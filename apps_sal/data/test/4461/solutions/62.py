h,w=map(int,input().split())
if h%3==0 or w%3==0:
  print(0)
else:
  temp=[w,h]
  if h%2==0 and w%2==0:
    temp.append(abs(int(w//3+1)*h-int(w-w//3-1)*int(h//2)))
    temp.append(abs(int(w//3)*h-int(w-w//3)*int(h//2)))        
    temp.append(abs(int(h//3+1)*w-int(h-h//3-1)*int(w//2)))
    temp.append(abs(int(h//3)*w-int(h-h//3)*int(w//2)))  
  elif h%2==0:
    temp.append(max(int(h//3*w),int(h-h//3)*int(w//2),int(h-h//3)*int(w//2+1))-min(int(h//3*w),int(h-h//3)*int(w//2),int(h-h//3)*int(w//2+1)))
    temp.append(max(int(h//3+1)*w,int(h-h//3-1)*int(w//2),int(h-h//3-1)*int(w//2+1))-min(int(h//3+1)*w,int(h-h//3-1)*int(w//2),int(h-h//3-1)*int(w//2+1)))
    temp.append(abs(int(w//3+1)*h-int(w-w//3-1)*int(h//2)))
    temp.append(abs(int(w//3)*h-int(w-w//3)*int(h//2)))             
  elif w%2==0:
    temp.append(max(int(w//3*h),int(w-w//3)*int(h//2),int(w-w//3)*int(h//2+1))-min(int(w//3*h),int(w-w//3)*int(h//2),int(w-w//3)*int(h//2+1)))
    temp.append(max(int(w//3+1)*h,int(w-w//3-1)*int(h//2),int(w-w//3-1)*int(h//2+1))-min(int(w//3+1)*h,int(w-w//3-1)*int(h//2),int(w-w//3-1)*int(h//2+1)))
    temp.append(abs(int(h//3+1)*w-int(h-h//3-1)*int(w//2)))
    temp.append(abs(int(h//3)*w-int(h-h//3)*int(w//2)))                
  else:
    temp.append(max(int(h//3*w),int(h-h//3)*int(w//2),int(h-h//3)*int(w//2+1))-min(int(h//3*w),int(h-h//3)*int(w//2),int(h-h//3)*int(w//2+1)))
    temp.append(max(int(h//3+1)*w,int(h-h//3-1)*int(w//2),int(h-h//3-1)*int(w//2+1))-min(int(h//3+1)*w,int(h-h//3-1)*int(w//2),int(h-h//3-1)*int(w//2+1)))
    temp.append(max(int(w//3*h),int(w-w//3)*int(h//2),int(w-w//3)*int(h//2+1))-min(int(w//3*h),int(w-w//3)*int(h//2),int(w-w//3)*int(h//2+1)))
    temp.append(max(int(w//3+1)*h,int(w-w//3-1)*int(h//2),int(w-w//3-1)*int(h//2+1))-min(int(w//3+1)*h,int(w-w//3-1)*int(h//2),int(w-w//3-1)*int(h//2+1)))
  print(min(temp))
