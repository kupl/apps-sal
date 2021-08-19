from collections import Counter
n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)  # カードの値をカウント
ans = len(cnt)  # 存在する値の数をカウント
if ans % 2 == 0:
    print(ans - 1)  # 存在する値の数が偶数であれば1回取り除く必要があるため-1をする
else:
    print(ans)  # 奇数の場合はそのまま
