import collections
import sys
input = sys.stdin.readline


def main():
    words = []
    word_dict = []
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    answers = []
    word_dict = collections.Counter(words)
    max_count = max(word_dict.values())
    [answers.append(values) for (values, counts) in word_dict.most_common() if counts == max_count]
    for answer in sorted(answers):
        print(answer)


def __starting_point():
    main()


__starting_point()
