#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#ifdef LOCAL_DEFINE
#pragma GCC optimize ("Ofast")
#pragma GCC target ("avx2")
#endif

int val(int s){
  int sum=0;
  while(s){
    sum += s%10;
    s/=10;
  }
  return sum*sum*sum;
}

void solve(){
	int n, s; cin >> n >> s;
	vector<int> v(n);
	for(int i = 0; i < n; i++){
	  cin >> v[i];
	}
	/*
	  dp[ind][str] = XV
	  dp[i][str+val(str)] = dp[i-1][str]
	  dp[i][str] = dp[i-1][str] + str*v[i]
	*/
	map<pair<int, int>, int> dp;
	dp.insert({{0, s}, s*v[0]});
	dp.insert({{0, s+val(s)}, 0});
	//cerr << s+val(s) << '\n';
	int ans = s*v[0];
	//for(int o = 1; o < n; o++){
	for(auto j: dp){
			int i = j.first.first, k = j.first.second;
	    if(i+1>n-1) break;

	    //if(dp.find({i+1, k+val(k)})==dp.end()) dp[{i+1, k+val(k)}] = 0;
			//if(dp.find({i+1, k})==dp.end()) dp[{i+1, k}] = 0;

	    dp[{i+1, k+val(k)}] = max(dp[{i+1, k+val(k)}], dp[{i, k}]);
	    dp[{i+1, k}] = max(dp[{i+1, k}], dp[{i, k}] + (k*v[i+1]));
	    //cerr << i << ' ' << dp[{i, k}] + (k*v[i]) << '\n';
	    ans = max(ans, max(dp[{i+1,k}], dp[{i+1,k+val(k)}]));
	}
	//}
	cout << ans << '\n';
}

int main() {
#ifdef LOCAL_DEFINE
	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; t=1;// cin >> t;
	while(t--) solve();  

#ifdef LOCAL_DEFINE
	cerr << "\nTime Elapsed: " << 1.0 * clock()/CLOCKS_PER_SEC << " s.\n";
#endif
}



