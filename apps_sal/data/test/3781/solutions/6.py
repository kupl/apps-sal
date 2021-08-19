from collections import Counter
T = int(input())
for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    if N % 2 == 1:
        # firはnim=0をsecはnim!=0を目指す。
        # ここで最初firは一つコインの山をつくるので、secはできているコインの山に現存する最大値を放り込み続ければ
        # その一つの山を無限に最大化でき、nim!=0を保証できる。
        print("Second")
    else:
        # firはnim!=0をsecはnim=0を目指す。
        # firは最初フラットな状態に遭遇し、コインの山を作ることになる。しかし、一度secがコインを置いて均衡を崩すことになれば、
        # firはできているコインの山に現存する最大値を放り込み続ければ、その一つの山を無限に最大化でき、nim!=0を保証できる。
        # 他方できない時は延々に均衡が崩れない時、つまり同じコインの袋が偶数個あるときのみとなる。
        flag = 0
        c = Counter(a)
        val = list(c.values())
        for j in val:
            if j % 2 == 1:
                flag = 1
                break
        if flag == 1:
            print("First")
        else:
            print("Second")
