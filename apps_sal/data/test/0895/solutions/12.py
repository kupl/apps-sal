def halyava(lst, t):
    count = 1
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst)[j] - sorted(lst)[i] <= t:
                count = max(j - i + 1, count)
    return count


n = int(input())
b = [int(x) for x in input().split()]
T = int(input())
print(halyava(b, T))
