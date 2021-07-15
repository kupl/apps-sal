from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    h, w, d = map(int, input().split())

    x = [0] * (h*w)
    y = x.copy()
    for i in range(h):
        a = list(map(int, input().split()))
        for j in range(w):
            x[a[j] - 1] = i
            y[a[j] - 1] = j

    # 累積和
    cost = [[0] for _ in range(d)]
    for i in range(d, h*w):
        cost[i%d].append(cost[i%d][-1] + abs(x[i]-x[i-d]) + abs(y[i]-y[i-d]))

    ans = []
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ans.append(cost[r%d][r//d] - cost[l%d][l//d])

    for i in ans:
        print(i)

main()
