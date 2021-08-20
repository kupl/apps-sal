(n, z, w) = map(int, input().split())
a = list(map(int, input().split()))
'\nxの選択肢は2つ。最後を取ってwと比較するか、最後から2番目を取って最後と比較する\n'
if n < 2:
    ans = abs(a[-1] - w)
else:
    ans = max(abs(a[-2] - a[-1]), abs(a[-1] - w))
print(ans)
