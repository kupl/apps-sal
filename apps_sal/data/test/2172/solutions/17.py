
def intput():
    return [int(x) for x in input().split(" ")]


def main(lecture, mapping):
    ans = []
    for word in lecture:
        ans.append(mapping[word])
    print(' '.join(ans))


def parse():
    _, words = intput()
    mapping = {}

    for _ in range(words):
        l1, l2 = input().split(" ")
        lm = l2 if len(l2) < len(l1) else l1
        mapping[l1] = lm

    lecture = input().split(" ")
    return lecture, mapping


main(*parse())
