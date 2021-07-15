def main():
    t = int(input())
    for i in range(t):
        a, b, k = map(int, input().split())
        pos = (a - b) * (k // 2)
        pos += a * (k % 2)
        print(pos)

main()
