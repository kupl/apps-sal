def read_ints():
    return list(map(int, input().split()))


n_messages, n_visible = read_ints()

refs = read_ints()

NO_REF = -1

refs = [i - 1 for i in refs]

read = [0] * n_messages


def messages_seen_at(index):
    return 1 + min(index, n_visible) + min(n_messages - index - 1, n_visible)


def intersection_seen(index, reference):
    if index <= reference:
        print("NOoooooooooo")

    def segment(index):
        return (max(0, index - n_visible), min(reference + n_visible, n_messages - 1))

    a, b = segment(reference)
    c, d = segment(index)

    return max(b - c + 1, 0)


def get_read(index):
    if refs[index] == NO_REF:
        read[index] = messages_seen_at(index)
    else:
        reads_by_ref = read[refs[index]]
        read[index] = reads_by_ref + messages_seen_at(index) - intersection_seen(index, refs[index])
    return read[index]


for i in range(n_messages):
    get_read(i)

print(' '.join(map(str, read)))
