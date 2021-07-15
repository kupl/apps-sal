def main():
    n, k = map(int, input().split(" "))
    data = sorted(int(input()) for _ in range(n))
    print(min([data[i+k-1] - data[i] for i in range(n-k+1)]))
main()
