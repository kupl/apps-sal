import sys

def main():
    s=sys.stdin.readline().rstrip()
    result=0
    
    for i in range(len(s)-1):
        if s[i:i+2]=='VK': result+=1
    
    if s.startswith('KK') or s.endswith('VV') or 'VKKK' in s or 'VVV' in s: result+=1
    
    sys.stdout.write(str(result)+'\n')
    
main()


