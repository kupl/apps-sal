import sys;

class MyReader:
#    file = null;
    def __init__(self):
        filename = "file.in";
        if self.isLocal():
            self.file = open(filename);
        self.str = [""];
        self.ind = 1;
            
    def isLocal(self):
        return len(sys.argv) > 1 and sys.argv[1] == "SCHULLZ";

    def nextString(self):
        if self.isLocal():
            return self.file.read();
        else:
            return input();
        
    def nextInt(self):
        return int(self.nextToken());

    def nextToken(self):
        if (self.ind >= len(self.str)):
            self.ind = 0;
            self.str = self.nextString().split();
        self.ind += 1;
        return self.str[self.ind - 1];



rdr = MyReader();

n = rdr.nextInt();
k = rdr.nextInt();

a = [];
isAwake = [];
missed = [];

for i in range (0, n):
    a.append(rdr.nextInt());
    
awaken = 0;

for i in range (0, n):
    isAwake.append(rdr.nextInt());
    missed.append(0);
    if (0 == isAwake[i]):
        missed[i] = a[i];
    else:
        awaken += a[i];
        missed[i] = 0;

tres = 0;
for i in range(0, k):
    tres += missed[i];

res = tres;

for i in range(k, n):
    tres -= missed[i - k];
    tres += missed[i];
    res = max(res, tres);

    
sys.stdout.write(str(res + awaken));

sys.stdout.flush()
