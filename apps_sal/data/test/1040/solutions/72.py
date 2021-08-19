n = int(input())
s = input()

# 解説を見て、分かった。これは思いつかない。
# このような問題をこなさないといけない領域だ。
# いやーなるほど。面白い。

# この変数に代入していく
work = ''

for i in s:
    work += i
    if work[-3:] == 'fox':
        work = work[:-3]
print(len(work))
