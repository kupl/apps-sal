n = int(input())


def main(i):
    if i % 5 == 0 and i % 3 == 0:
        return 0
    elif i % 3 == 0:
        return 0
    elif i % 5 == 0:
        return 0
    else:
        return i


ans = 0
for i in range(n + 1):
    ans += main(i)
print(ans)
