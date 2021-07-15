#N人　K種類のお菓子
[N, K] = [int(i) for i in input().split()]

okasi = [0]*N #i番目の人が持っているお菓子の中で、種類番号が多いものに更新する

#お菓子K種類渡す
for k in range(K):
    num = int(input()) #お菓子の番号
    have = [int(i) for i in input().split()]
    for snuke in have:
        okasi[snuke-1] = num

#お菓子持ってない人を探す
print(okasi.count(0))
