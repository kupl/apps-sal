N, A, B, C = map(int, input().split())
ss = [input() for _ in range(N)]

history = []

def move_to_flatten(s):
    nonlocal A, B, C, history
    if s == "AB":
        if A >= B:
            A -= 1
            B += 1
            history.append("B")
        else:
            B -= 1
            A += 1
            history.append("A")
    elif s == "BC":
        if B >= C:
            B -= 1
            C += 1
            history.append("C")
        else:
            C -= 1
            B += 1
            history.append("B")
    elif s == "AC":
        if A >= C:
            A -= 1
            C += 1
            history.append("C")
        else:
            C -= 1
            A += 1
            history.append("A")
        

for i, s in enumerate(ss):
    zeros = (A, B, C).count(0)
    if zeros == 0:
        move_to_flatten(s)
    elif zeros == 1:
        if A + B + C == 2:
            if A == 0:
                if s == "BC":
                    if i+1 < N and 'B' in ss[i+1]: 
                        C -= 1
                        B += 1
                        history.append('B')
                    else:
                        B -= 1
                        C += 1
                        history.append('C')
                else:
                    move_to_flatten(s)
            elif B == 0:
                if s == "AC":
                    if i+1 < N and 'C' in ss[i+1]:
                        A -= 1
                        C += 1
                        history.append('C')
                    else:
                        C -= 1
                        A += 1
                        history.append('A')
                else:
                    move_to_flatten(s)
            elif C == 0:
                if s == "AB":
                    if i+1 < N and 'A' in ss[i+1]:
                        B -= 1
                        A += 1
                        history.append('A')
                    else:
                        A -= 1
                        B += 1
                        history.append('B')
                else:
                    move_to_flatten(s)    
        else:
            move_to_flatten(s)
    elif zeros == 2:
        if A != 0 and s == "BC":
            print("No")
            return
        elif B != 0 and s == "AC":
            print("No")
            return
        elif C != 0 and s == "AB":
            print("No")
            return
        move_to_flatten(s)
    else:
        print("No")
        return

print("Yes")
print(*history, sep = '\n')
