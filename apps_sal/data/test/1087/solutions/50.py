N, K = map(int, input().split())
As = list(map(int, input().split()))
bitK = K.bit_length()
ans = [0]*bitK
for a in As:
    for i in range(bitK):
        if not (a>>i)&1:
            ans[i] += 1

ans = ans[::-1]
string = ['0']*bitK
if bitK==0:
    print(sum(As))
else:
    for i, a in enumerate(ans):
        if a>=N/2:
            string[i] = '1'
            if int(''.join(string), 2)>K:
                string[i] = '0'
    num = int(''.join(string), 2)
    print(sum([x^num for x in As]))
