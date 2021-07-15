S = input()

ls = ["WB", "BW"]

cnt = 0
if S[0] == "W":
  i = 0
else:
  i = 1

for j in range(len(S)-1):
  if i == 0 and S[j:j+2] == "WB":
    cnt += 1
    i = 1
  if i == 1 and S[j:j+2] == "BW":
    cnt += 1
    i = 0
    
print(cnt)
