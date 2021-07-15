
def resolve():
    def check(arr):
        height = 0
        for b, h in arr:
            if height+b < 0:
                return False
            height += h
        return True

    N = int(input())
    plus = []
    minus = []
    total = 0
    for _ in range(N):
        # 1つのパーツを処理
        S = input()
        cum = 0 # 累積和(最高地点)
        bottom = 0 # 最下地点
        for s in S:
            if s == "(":
                cum += 1
            else:
                cum -= 1
            bottom = min(bottom, cum)

        total += cum
        if cum > 0:
            plus.append((bottom, cum))
        else:
            minus.append((bottom-cum, -cum))

    plus.sort(reverse=True)
    minus.sort(reverse=True)

    if check(plus) and check(minus) and total == 0:
        print("Yes")
    else:
        print("No")

def __starting_point():
    resolve()

__starting_point()
