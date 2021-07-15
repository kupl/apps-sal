class word:
    l, r = -1, -1

left_word = word()
right_word = word()

subs = input()
s = input()

pos = 0
for i in range(len(s)):
    if s[i] == subs[pos]:
        if pos == 0:
            left_word.l = i
        if pos == len(subs) - 1:
            left_word.r = i
            break
        
        pos += 1
 
pos = len(subs) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == subs[pos]:
        if pos == len(subs) - 1:
            right_word.r = i
        if pos == 0:
            right_word.l = i
            break                        
            
        pos -= 1   
        
print(max(0, right_word.l - left_word.r))


