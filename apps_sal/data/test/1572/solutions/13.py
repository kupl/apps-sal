def read_args():
    n = int(input())
    a = list(map(int, input().split()))
    return a, n


def get_good_segment_of_max_length(a, n):
    if n <= 2:
        return n
    count = 0
    current_count = 0
    for i in range(n - 2):
        if a[i] + a[i + 1] == a[i + 2]:
            current_count += 1
            if count < current_count:
                count = current_count
        else:
            current_count = 0
    return count + 2


def __starting_point():
    a, n = read_args()
    print(get_good_segment_of_max_length(a, n))
__starting_point()
