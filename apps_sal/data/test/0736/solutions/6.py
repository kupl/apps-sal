
def main(n, m):
    if n < m:
        return -1
    temp = int(n / 2) + n % 2
    while temp % m != 0 and temp < n:
        temp = temp + 1
    return temp if temp % m == 0 else -1


n, m = input().split(' ')
n, m = int(n), int(m)

print(main(n, m))
