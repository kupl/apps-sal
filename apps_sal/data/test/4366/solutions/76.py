# イルカはプログラミングコンテスト好きで、今日はAtCoderのコンテストに参加します。
# 現在時刻は、24時間表記(0:00 〜23:59) で A時ちょうどであり、
# コンテストがちょうど B時間後に始まります。
# コンテストの開始時刻は、24時間表記で何時ちょうどでしょうか?

# 制約
# 0 ≦ A, B ≦ 23
# A, B は整数である。

# 標準入力から A時、B時を取得する
hour_a,hour_b = list(map(int,input().split()))

# コンテストの開始時間を計算し出力する
contest_start_hour = 0  # コンテスト開始時間

contest_start_hour = hour_a + hour_b

if contest_start_hour >= 24:    # 日付変わってるよ～
    contest_start_hour -= 24

print(contest_start_hour)

