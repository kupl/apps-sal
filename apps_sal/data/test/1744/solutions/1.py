import math


def main():
    n, m = map(int, input().split())
    time = list(map(int, input().split()))
    ans = []
    total = 0
    counts = [0] * 100
    for i in range(n):
        if m - total >= time[i]:
            ans.append(0)
        else:
            count = 0
            new = total
            for j in range(99, -1, -1):
                if counts[j] > 0:
                    new -= counts[j] * (j + 1)
                    if m - new < time[i]:
                        count += counts[j]
                    else:
                        new += counts[j] * (j + 1)
                        count += math.ceil((time[i] + new - m) / (j + 1))
                        break
            ans.append(count)

        counts[time[i] - 1] += 1
        total += time[i]

    for i in ans:
        print(i, end=' ')


main()
