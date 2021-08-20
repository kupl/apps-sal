def solve():
    prev_last = -1
    count = 0
    n = int(input())
    for _ in range(n):
        (first, last) = input()
        if prev_last == -1 or prev_last == first:
            count += 1
        prev_last = last
    return count


print(solve())
