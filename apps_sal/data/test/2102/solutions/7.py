from collections import deque as _deque
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

    max_from_initially_selected_frets = max(frets[0] for frets in frets_by_notes_indices)
    for frets in frets_by_notes_indices:
        i_first_interesting_fret = 0
        while i_first_interesting_fret + 1 < len(frets) \
                and frets[i_first_interesting_fret + 1] <= max_from_initially_selected_frets:
            i_first_interesting_fret += 1
        frets[:] = frets[i_first_interesting_fret:]

    selected_frets = [frets[0] for frets in frets_by_notes_indices]
    selected_frets.sort()
    selected_frets = _deque(selected_frets)

    available_selections = _chain.from_iterable(
        list(zip(frets[1:], frets[0:]))
        for frets in frets_by_notes_indices
    )
    available_selections = sorted(available_selections)

    # defaultdict(int) is slower
    frets_to_unselect = dict()
    for frets in frets_by_notes_indices:
        for fret in frets:
            frets_to_unselect[fret] = 0

    min_selected_fret = selected_frets[0]
    max_selected_fret = max(selected_frets)
    result = max_selected_fret - min_selected_fret

    for new_fret, fret_to_unselect in available_selections:
        frets_to_unselect[fret_to_unselect] += 1
        _clean_deque_begin(selected_frets, frets_to_unselect)
        selected_frets.append(new_fret)

        min_selected_fret = selected_frets[0]
        max_selected_fret = new_fret
        result = min(result, max_selected_fret - min_selected_fret)

    return result


def _clean_deque_begin(deque, deletions_ns):
    while deque and deletions_ns[deque[0]] > 0:
        deleted_element = deque.popleft()
        deletions_ns[deleted_element] -= 1


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split()))


def __starting_point():
    main()


__starting_point()
