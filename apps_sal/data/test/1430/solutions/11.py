n,k=list(map(int, input().split()))
s=input()

def rle(string):
    _rle_str = string[0]
    _rle_cnt = 1
    _ans_l = []
    for _i in range(1, len(string)):
        if _rle_str == string[_i]:
            _rle_cnt += 1
        else:
            _ans_l.append([_rle_str, _rle_cnt])
            _rle_str = string[_i]
            _rle_cnt = 1
    _ans_l.append([_rle_str, _rle_cnt])
    return _ans_l

rle_s=rle(s)

ans=-1

left=0
wa=0

if rle_s[0][0]=="0":
    cnt=1
    wa=rle_s[0][1]
    right=1
else:
    cnt=0
    right=0

if len(rle_s)==1 and k>=1:
    print((rle_s[0][1]))
    return

while right<len(rle_s):
    # print(right, left, wa, cnt)
    if cnt==k:
        if rle_s[right][0]=="0":
            if rle_s[left][0]=="0":
                wa-=rle_s[left][1]
                cnt-=1
            else:
                wa-=rle_s[left][1]
            left+=1

        else:
            wa+=rle_s[right][1]
            right+=1
            ans=max(ans, wa)

    elif cnt<k:
        if rle_s[right][0]=="0":
            cnt+=1
            wa+=rle_s[right][1]
        else:
            wa+=rle_s[right][1]
        right+=1
        ans=max(ans, wa)

    else:
        if rle_s[left][0]=="0":
            wa-=rle_s[left][1]
            cnt-=1
        else:
            wa-=rle_s[left][1]
        left+=1

print(ans)

