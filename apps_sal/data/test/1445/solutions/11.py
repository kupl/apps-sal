

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n // 2):
        if i % 2 == 0:
            a[i], a[n - i - 1] = a[n - i - 1], a[i]
    print(*a)

main()
