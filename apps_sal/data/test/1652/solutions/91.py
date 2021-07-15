S = list(input())

i = len(S)-1
while i >= 4:
    if S[i-4:i+1] == ['d', 'r', 'e', 'a', 'm'] or S[i-4:i+1] == ['e', 'r', 'a', 's', 'e']:
        i -= 5
    elif i-5 >= 0 and S[i-5:i+1] == ["e", "r", "a", "s", "e", "r"]:
        i -= 6
    elif i-6 >= 0 and S[i-6:i+1] == ["d", "r", "e", "a", "m", "e", "r"]:
        i -= 7
    else:
        break
        
if i == -1:
    print("YES")
else:
    print("NO")
