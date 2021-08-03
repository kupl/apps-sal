N, M = map(int, input().split())
s = [list(map(lambda x:int(x) - 1, input().split()[1:])) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**N):  # 全てのスイッチの (on, off) の組み合わせ
    # 電球jが点灯する条件：繋がっているk_j個のスイッチのうち、onの個数を2で割った余りがp_jに等しい
    bulb_num = 0  # 点灯する電球の個数
    for j in range(M):  # ある (on, off) の組において、点灯する電球の個数を求める
        on_num = 0  # 電球jに繋がっているスイッチのうち、onの個数
        for k in range(N):
            # スイッチkがon かつ、電球jとスイッチkが繋がっているならば：
            if i >> k & 1 and k in s[j]:
                on_num += 1
        if (on_num - p[j]) % 2 == 0:
            bulb_num += 1
    if bulb_num == M:
        ans += 1

print(ans)
