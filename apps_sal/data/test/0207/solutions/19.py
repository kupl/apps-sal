# coding: utf-8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 1 and a[0] % 2 == 1 and a[-1] % 2 == 1:
        return "Yes"
    return "No"

print(main())

