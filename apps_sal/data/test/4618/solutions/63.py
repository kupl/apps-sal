s=input();k=int(input());print(sorted({s[i:i+j]for i in range(len(s))for j in range(1,k+1)})[k-1])
