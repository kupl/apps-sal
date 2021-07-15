def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        values = list(map(int, input().split()))
        answer = [0 for i in range(n)]
        for i in range(n):
            if i % 2 == 0:
                answer[i] = -values[i + 1]
            else:
                answer[i] = values[i-1]
        print(*answer)
main()
