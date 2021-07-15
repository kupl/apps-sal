import fileinput
import sys

class MyInput(object) :
    def __init__(self,default_file=None) :
        self.fh = sys.stdin
        if (len(sys.argv) >= 2) : self.fh = open(sys.argv[1])
        elif default_file is not None : self.fh = open(default_file)
    def getintline(self,n=-1) : 
        ans = tuple(int(x) for x in self.fh.readline().rstrip().split())
        if n > 0 and len(ans) != n : raise Exception('Expected %d ints but got %d in MyInput.getintline'%(n,len(ans)))
        return ans
    def getfloatline(self,n=-1) :
        ans = tuple(float(x) for x in self.fh.readline().rstrip().split())
        if n > 0 and len(ans) != n : raise Exception('Expected %d floats but got %d in MyInput.getfloatline'%(n,len(ans)))
        return ans
    def getstringline(self,n=-1) :
        ans = tuple(self.fh.readline().rstrip().split())
        if n > 0 and len(ans) != n : raise Exception('Expected %d strings but got %d in MyInput.getstringline'%(n,len(ans)))
        return ans
    def getbinline(self,n=-1) :
        ans = tuple(int(x,2) for x in self.fh.readline().rstrip().split())
        if n > 0 and len(ans) != n : raise Exception('Expected %d bins but got %d in MyInput.getbinline'%(n,len(ans)))
        return ans

def compress(s) :
    s2 = [s[0]]
    for c in s :
        if c != s2[-1] : s2.append(c)
    return "".join(s2)

def __starting_point():
    myin = MyInput()
    (s,) = myin.getstringline(1)
    ## Make sure there are a's followed by b's followed by c's
    ## Make sure the count of cs either equals count of as or count of bs
    s1 = compress(s)
    ans = "NO"
    if s1 == 'abc' and ( s.count('c') == s.count('a') or s.count('c') == s.count('b') ) : ans = "YES"
    print(ans)


__starting_point()
