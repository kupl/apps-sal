from collections import Counter


def main():
    n = int(input())
    data = Counter(int(input()) for _ in range(n))
    ans = sum(num % 2 != 0
              for num in data.values()
              )
    print(ans)


main()
