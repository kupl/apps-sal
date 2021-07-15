elems = int(input())
data = list(map(int, input().split()))
data.append(float("-inf"))

def find_seq_breaks():
    nonlocal elems
    nonlocal data
    seq_spans = []
    sequence_idx = 0
    longest_span = 0
    for i in range(1, elems + 1):
        if data[i] <= data[i - 1]:
            seq_range = [sequence_idx, i - 1]
            seq_spans.append(seq_range)

            diff = i - sequence_idx
            if (longest_span < diff):
                longest_span = diff

            sequence_idx = i
    return (seq_spans, longest_span)

def parse_seqs(seq_spans, longest_span):
    nonlocal data
    nonlocal elems

    if len(seq_spans) > 1:
        longest_span += 1

    for i in range(1, len(seq_spans)):
        one_past = seq_spans[i][0]
        if one_past >= 2 or one_past <= elems - 1:
            #look at values before and after num that broke seq
            r = data[one_past] - data[one_past-2]
            r2 = data[one_past + 1] - data[one_past - 1]
            candidate = seq_spans[i][1] - seq_spans[i - 1][0] + 1
            if r >= r2:
                if r >= 2:
                   if longest_span < candidate:
                       longest_span = candidate
            elif r2 >= 2:
                if r2 >= 2:
                    if longest_span < candidate:
                        longest_span = candidate
    return longest_span

d = find_seq_breaks()
print(parse_seqs(d[0], d[1]))

