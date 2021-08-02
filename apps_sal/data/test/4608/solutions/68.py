def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    cnt = 0
    tmp = 1
    while cnt <= 100001:
        tmp = a[tmp - 1]
        cnt += 1
        if tmp == 2:
            return cnt
        elif tmp == 1:
            return -1

    return -1


print((main()))
