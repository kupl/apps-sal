def main():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    first_half = sum(array[:n])
    second_half = sum(array[n:])

    if first_half == second_half:
        print(-1)
        return

    for i in array:
        print(i, end=' ')


main()
