# 解説を見て解いた
# 空文字列に1文字ずつ足していき末尾3文字がfoxなら取り除けばよい

N = int(input())
s = input()

ps = ''

for c in s:
    ps += c
    if ps[len(ps)-3:len(ps)] == 'fox':
        ps = ps[0:len(ps)-3]

print(len(ps))
