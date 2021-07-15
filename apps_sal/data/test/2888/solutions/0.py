#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define inf 100000000000000
typedef long long ll;
#define mp make_pair
#define f first 
#define s second
ll xp[5005];
ll train[5005];
ll dp[5005][5005];
int n;
ll power(ll x,ll y){
    ll res=1;
    while (y){
        if (y & 1){
            res=res*x; 
        }
        x=x*x;
        y=y>>1;
    }
    return res;
}
ll cube(ll x){
    ll res=x,sum=0;
    while(x!=0){
        sum+=(x%10);
        x=x/10;
    }
    res+=power(sum,3);
    return res;
}
ll max_xp(int i,int r){
    if(i>n){
        return 0;
    }
    if(dp[i][r]!=-1){
        return dp[i][r];
    }
    ll maxi=0;
    if(r<=n){
        maxi=max_xp(i+1,r+1);
    }
    maxi=max(maxi,max_xp(i+1,r)+xp[i]*train[r]);
    return dp[i][r]=maxi;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll s;
	cin>>n>>s;
	for(int i=1;i<=n;i++){
	    cin>>xp[i];
	}
	memset(dp,-1,sizeof(dp));
	train[0]=s;
	for(int i=1;i<=n;i++){
	    train[i]=cube(train[i-1]);
	}
	cout<<max_xp(1,0)<<"\n";
	return 0;
}
