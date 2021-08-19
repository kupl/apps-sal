def gcd(a, b):
    return gcd(b, a % b) if b else a


def main():
    (n, m, l) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = [i > l for i in arr]
    total = 0
    for i in range(len(brr)):
        if brr[i] and (not i or not brr[i - 1]):
            total += 1
    for i in range(m):
        s = input()
        if s[0] == '0':
            print(total)
        else:
            (_, a, b) = list(map(int, s.split()))
            a -= 1
            arr[a] += b
            if arr[a] > l and (not brr[a]):
                brr[a] = True
                if (a > 0 and brr[a - 1]) and (a < len(brr) - 1 and brr[a + 1]):
                    total -= 1
                elif (a == 0 or (a > 0 and (not brr[a - 1]))) and (a == len(brr) - 1 or (a < len(brr) - 1 and (not brr[a + 1]))):
                    total += 1


main()
