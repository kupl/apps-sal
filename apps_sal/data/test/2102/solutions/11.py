from itertools import chain as _chain
import sys as _sys


def main():
    a_seq = tuple(_read_ints())
    n, = _read_ints()
    notes = tuple(_read_ints())
    result = find_minimal_melody_difficulty(a_seq, notes)
    print(result)


def find_minimal_melody_difficulty(strings_values, notes):
    strings_values = set(strings_values)
    strings_values = sorted(strings_values, reverse=True)
    if len(strings_values) == 1:
        return max(notes) - min(notes)

    frets_by_notes_indices = [[note - x for x in strings_values] for note in notes]
    # frets_by_notes_indices[i_note] is sorted for every correct i_note
    del strings_values
    del notes

    max_initially_selected_fret = max(frets[0] for frets in frets_by_notes_indices)
    for frets in frets_by_notes_indices:
        i_first_interesting_fret = 0
        while i_first_interesting_fret + 1 < len(frets) \
                and frets[i_first_interesting_fret + 1] <= max_initially_selected_fret:
            i_first_interesting_fret += 1
        frets[:] = frets[i_first_interesting_fret:]

    sorted_frets = sorted(_chain.from_iterable(frets_by_notes_indices))

    initially_selected_frets = [frets[0] for frets in frets_by_notes_indices]
    min_initially_selected = min(initially_selected_frets)
    i_first_selected = sorted_frets.index(min_initially_selected)
    while i_first_selected + 1 < len(sorted_frets) \
            and sorted_frets[i_first_selected + 1] == min_initially_selected:
        i_first_selected += 1
    i_first_selected -= initially_selected_frets.count(min_initially_selected) - 1
    i_last_selected = i_first_selected + len(initially_selected_frets) - 1

    available_selections = _chain.from_iterable(
        list(zip(frets[1:], frets[0:]))
        for frets in frets_by_notes_indices
    )
    available_selections = sorted(available_selections)

    # TODO: can replace it with indices_to_unselect
    # defaultdict(int) is slower
    frets_to_unselect = dict()
    for frets in frets_by_notes_indices:
        for fret in frets:
            frets_to_unselect[fret] = 0

    result = sorted_frets[i_last_selected] - sorted_frets[i_first_selected]

    for new_fret, fret_to_unselect in available_selections:
        frets_to_unselect[fret_to_unselect] += 1
        i_first_selected = _shift_index_skipping(sorted_frets, i_first_selected, frets_to_unselect)
        i_last_selected += 1
        current_maxmin_difference = sorted_frets[i_last_selected] - sorted_frets[i_first_selected]
        if current_maxmin_difference < result:
            result = current_maxmin_difference

    return result


def _shift_index_skipping(sorted_seq, index, deletions_ns):
    while index < len(sorted_seq) and deletions_ns[sorted_seq[index]] > 0:
        deleted_element = sorted_seq[index]
        index += 1
        deletions_ns[deleted_element] -= 1
    return index


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split()))


def __starting_point():
    main()


__starting_point()
