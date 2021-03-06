K = int(input())
'\n愚直解\nNを2~50までは試せるけど、各要素の値は何にすればいいかよくわからない。\nなので、全探索的な解き方は期待できない。\n\n一つからN引いて、残りに＋１するので、一回の操作で全体の合計から１減っていることになる\nなので、開始時点で全体の合計は、(N-1)*N + K ~ N*N+K になるのか?\n\nある操作を繰り返して最後に～系の問題は、最後から操作を逆におこなって最初の状態に戻るようにすると解けることがおおい\n今回はK回の操作の後に数列の最大値が N-1 以下になるので、N-1から開始して、ある要素にN足して全体から１引く、をK回やればよい。\nNは50までなので、とりあえず５０とする（小さすぎなければよいと判断）\n\n操作が配列の要素すべてに一回ずつ行われたとき、NふえてN-1減るので、1増えただけになる\n'
N = 50
ans = [49] * 50
cnt_all = K // N
rem = K % N
for i in range(N):
    if i < rem:
        ans[i] += cnt_all + N - (rem - 1)
    else:
        ans[i] += cnt_all - rem
print(50)
print(*ans)
