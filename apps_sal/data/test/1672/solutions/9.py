# have last digit of previous entry
# for every line in the input check the first digit
# if digits are same
# increment count

def solve():
    prev_last = -1
    count = 0
    n = int(input())
    for _ in range(n):
        first, last = input()
        if prev_last == -1 or prev_last == first:
            count += 1
        prev_last = last
    return count


print(solve())
