def func(a, b):
    if b % a != 0:
        return -1
    else:
        store = b // a
        count = 0
        while store % 2 == 0:
            store //= 2
            count += 1
        while store % 3 == 0:
            store //= 3
            count += 1
        if store == 1:
            return count
        else:
            return -1


def main():
    arr = input().split()
    print(func(int(arr[0]), int(arr[1])))


main()
