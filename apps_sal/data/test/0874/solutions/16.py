def main():
    n = int(input())
    if n & 1:
        return (-1,)
    return list(range(n, 0, -1))


print(*main())
