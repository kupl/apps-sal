def number_of_inversions(l):
    counter = 0
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            counter += 1
    return counter


def is_right_choice(l, k):
    return number_of_inversions(l) == k


def make_k_inversions(n, k):
    length_of_inverted = k + 1
    length_of_non_inverted = n - length_of_inverted
    non_inverted = list(range(1, length_of_non_inverted + 1))
    inverted = list(range(length_of_non_inverted + 1, n + 1))
    inverted.reverse()
    return non_inverted + inverted


def main():
    first_line = input()
    first_line = first_line.split()
    n = int(first_line[0])
    k = int(first_line[1])
    l = make_k_inversions(n, k)
    output = ''
    for item in l:
        output += str(item) + ' '
    print(output)


main()
