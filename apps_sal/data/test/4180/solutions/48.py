N = int(input())
note = 1000

reminder = str(N/note)[-1]
if int(reminder) == 0:
    result = 0
else:
    reminder = (N//note)+1
    result = (int(reminder * note)) - N
    
print(result)
