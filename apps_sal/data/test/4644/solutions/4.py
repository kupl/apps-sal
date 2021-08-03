def iinput():
    return [int(x) for x in input().split()]


def main():
    n = int(input())
    data = iinput()
    count = 0
    for i in range(n):
        if data[i] % 2 == 1:
            count += 1
    if count == 0 or (count == n and n % 2 == 0):
        return 'NO'
    else:
        return 'YES'


for t in range(int(input())):
    print(main())
