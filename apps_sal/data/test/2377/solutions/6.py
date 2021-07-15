
def main():
    with open(0) as f:
        N, H = list(map(int, f.readline().split()))
        ab = list(map(int, f.read().split()))
    max_slash = max(ab[0::2])
    throw = sorted([x for x in ab[1::2] if x > max_slash], reverse=True)
    cnt = 0
    for t in throw:
        if H <= 0:
            break
        H += -t
        cnt += 1
    if H > 0:
        cnt += (H+max_slash-1)//max_slash
    print(cnt)

main()


