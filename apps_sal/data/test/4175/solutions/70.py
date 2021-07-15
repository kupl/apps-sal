N = int(input())

used_word_set = set()

last_char = '@'
for i in range(N):
    w = input()
    
    if i != 0 and (w in used_word_set or last_char != w[0]):
        print("No")
        return
        
    last_char = w[-1]
    used_word_set.add(w)
    
print("Yes")
