S = input()
T = input()

# len:ﾘｽﾄの値（何文字入ってるか）の使う
# for i in range(): ()には繰り返したい回数を入れる。

for i in range(len(S)):
    if S[i:] + S[:i] == T:  # SとTに使われてるアルファべットが同じという証明
        print('Yes')
        return              
# elseでは出来なかった。一旦exitでる。
print('No')
