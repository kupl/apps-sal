MOD = 10**9 + 7
N = int(input())
s1 = input()
s2 = input()

result = 1

s_index = 0

# とりあえず一番左のドミノを見る
# 縦置き
if s1[s_index] == s2[s_index]:
    result *= 3
    s_index += 1
    prev_verticalp = True
else:
    result *= 6
    s_index += 2
    prev_verticalp = False

# 二番目以降は前回縦置きか横置きかで変わる
while s_index < N:
    if prev_verticalp:
        if s1[s_index] == s2[s_index]:
            result = (result * 2) % MOD
            s_index += 1
            prev_verticalp = True
        else:
            result = (result * 2) % MOD
            s_index += 2
            prev_verticalp = False
    
    else:
        if s1[s_index] == s2[s_index]:
            s_index += 1
            prev_verticalp = True
        else:
            result = (result * 3) % MOD
            s_index += 2
            prev_verticalp = False

print(result)


